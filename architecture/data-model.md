# Data Model — miles-app

# Main Entities

## User

Represents a platform user.

### Fields

```txt
id
name
email
created_at
updated_at
```

---

## Alert

Represents a monitoring configuration.

### Fields

```txt
id
user_id
origin_airport
destination_airport
destination_city
destination_country
start_date
end_date
flexibility_days
cabin_class
passengers
max_miles
max_cash_fee
programs
nonstop_only
frequency_minutes
active
created_at
updated_at
```

---

## SearchExecution

Represents a scraper execution.

### Fields

```txt
id
program
search_input
status
started_at
finished_at
error_message
```

---

## RawSearchResult

Stores raw scraper output.

### Fields

```txt
id
execution_id
provider
raw_payload
captured_at
```

---

## SearchResult

Normalized result.

### Fields

```txt
id
execution_id
provider
airline
origin
destination
departure_date
return_date
miles_price
cash_fee
currency
cabin_class
stops
flight_duration
availability
source_url
captured_at
```

---

## Notification

Stores notification history.

### Fields

```txt
id
user_id
alert_id
search_result_id
channel
status
sent_at
```

---

# Initial Relationships

```txt
User 1:N Alert
Alert 1:N Notification
SearchExecution 1:N RawSearchResult
SearchExecution 1:N SearchResult
SearchResult 1:N Notification
```

---

# Data Principles

## Preserve Raw Data

Never discard raw scraper payloads.

## Normalize Early

Convert all providers to a unified format.

## Immutable Search Results

Search results should not be mutated after creation.

## Track Capture Time

Every result must contain capture timestamps.
