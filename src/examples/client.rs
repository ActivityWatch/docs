use aw_client_rust::AwClient;
use aw_models::{Bucket, Event};
use chrono::TimeDelta;
use serde_json::{Map, Value};

async fn create_bucket(
    aw_client: &AwClient,
    bucket_id: String,
    event_type: String,
) -> Result<(), Box<dyn std::error::Error>> {
    let res = aw_client
        .create_bucket(&Bucket {
            id: bucket_id,
            bid: None,
            _type: event_type,
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
    let event_type = "dummy_data".to_string();

    create_bucket(&aw_client, bucket_id.clone(), event_type)
        .await
        .unwrap();

    let sleeptime = 1.0;
    for i in 0..5 {
        // Create a sample event to send as heartbeat
        let mut heartbeat_data = Map::new();
        heartbeat_data.insert("label".to_string(), Value::String("heartbeat".to_string()));

        let now = chrono::Utc::now();

        let heartbeat_event = Event {
            id: None,
            timestamp: now,
            duration: TimeDelta::seconds(1),
            data: heartbeat_data,
        };

        println!("Sending heartbeat event {}", i);
        // The rust client does not support queued heartbeats, or commit intervals
        aw_client
            .heartbeat(&bucket_id, &heartbeat_event, sleeptime + 1.0)
            .await
            .unwrap();

        // Sleep a second until next heartbeat (eventually drifts due to time spent in the loop)
        tokio::time::sleep(tokio::time::Duration::from_secs_f64(sleeptime)).await;
    }

    // Sleep a bit more to allow the last heartbeat to be sent
    tokio::time::sleep(tokio::time::Duration::from_secs_f64(sleeptime)).await;

    // Synchoronous example, insert an event
    let mut event_data = Map::new();
    event_data.insert(
        "label".to_string(),
        Value::String("non-heartbeat event".to_string()),
    );
    let now = chrono::Utc::now();
    let event = Event {
        id: None,
        timestamp: now,
        duration: TimeDelta::seconds(1),
        data: event_data,
    };
    aw_client.insert_event(&bucket_id, &event).await.unwrap();

    // fetch the last 10 events
    // should include the first 5 heartbeats and the last event
    let events = aw_client
        .get_events(&bucket_id, None, None, Some(10))
        .await
        .unwrap();
    println!("Events: {:?}", events);

    // Delete the bucket
    aw_client.delete_bucket(&bucket_id).await.unwrap();
}
