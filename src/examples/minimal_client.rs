use aw_client_rust::AwClient;
use aw_models::{Bucket, Event};
use chrono::TimeDelta;
use serde_json::{Map, Value};

async fn create_bucket(
    aw_client: &AwClient,
    bucket_id: String,
) -> Result<(), Box<dyn std::error::Error>> {
    let res = aw_client
        .create_bucket(&Bucket {
            id: bucket_id,
            bid: None,
            _type: "dummy_data".to_string(),
            data: Map::new(),
            metadata: Default::default(),
            last_updated: None,
            hostname: "".to_string(),
            client: "test-client".to_string(),
            created: None,
            events: None,
        })
        .await?;

    Ok(res)
}

#[tokio::main]
async fn main() {
    let port = 5666; // the testing port 
    let aw_client = AwClient::new("localhost", port, "test-client").unwrap();
    let bucket_id = format!("test-client-bucket_{}", aw_client.hostname);

    create_bucket(&aw_client, bucket_id.clone()).await.unwrap();

    let mut shutdown_data = Map::new();
    shutdown_data.insert(
        "label".to_string(),
        Value::String("some interesting data".to_string()),
    );

    let now = chrono::Utc::now();
    let shutdown_event = Event {
        id: None,
        timestamp: now,
        duration: TimeDelta::seconds(420),
        data: shutdown_data,
    };
    aw_client.insert_event(&bucket_id, &shutdown_event).await.unwrap();

    let events = aw_client.get_events(&bucket_id, None, None, Some(1)).await.unwrap();
    print!("{:?}", events); // prints a single event

    aw_client.delete_bucket(&bucket_id).await.unwrap();
}
