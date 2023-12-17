#!/usr/bin/env sh

# Создаем синк для ClickHouse
pulsar/bin/pulsar-admin sinks create \
  --sink-type 'jdbc-clickhouse' \
  --name "trips-connector" \
  --inputs "persistent://public/default/clickhouse-test" \
  --tenant "public" \
  --sink-config-file /configs/clickhouse-connector.yaml \
  --parallelism 1