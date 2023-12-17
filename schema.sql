CREATE TABLE IF NOT EXISTS trips
(
    trip_id     INT,
    client_name String,
    price       UInt64
) ENGINE = MergeTree()
      ORDER BY trip_id;


CREATE TABLE trips_aggregated_mv
(
    client_name String,
    trip_count  UInt64
) ENGINE = SummingMergeTree()
      ORDER BY (client_name);


create materialized view trips_mv to trips_aggregated_mv as
select client_name,
       count() as trip_count
from trips
group by client_name;