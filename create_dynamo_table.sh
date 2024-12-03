if aws dynamodb describe-table --table-name EventsTable >/dev/null 2>&1; then
    echo "Table Already Exists"
    exit 0
fi
aws dynamodb create-table \
    --table-name EventsTable \
    --key-schema AttributeName=event_id,KeyType=HASH \
    --attribute-definitions AttributeName=event_id,AttributeType=S \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 > /dev/null || exit 1
echo "DONE"

