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

### Validation Rules

```txt
user_id: required until authentication exists
origin_airport: required IATA code, normalized uppercase, exactly 3 characters
destination_airport: required IATA code, normalized uppercase, exactly 3 characters
start_date/end_date: required, end_date must be on or after start_date
flexibility_days: 0 to 30
cabin_class: economy, premium_economy, business or first
passengers: 1 to 9
max_miles: greater than 0
max_cash_fee: optional, greater than or equal to 0 when provided
programs: at least one loyalty program name
frequency_minutes: 15 to 10080
active: defaults to true
```

### API Contract

Initial local/dev API endpoints:

```txt
POST /alerts
GET /alerts
GET /alerts/{id}
PATCH /alerts/{id}
DELETE /alerts/{id}
```

Authentication is not implemented yet. Alert ownership is represented by the
explicit `user_id` field until a User/authentication ticket defines the source
of the authenticated principal.

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
