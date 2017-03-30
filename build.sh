#!/bin/bash

set -euxo pipefail

echo "Building protobuf files"
rm -rf ./lbryschema/schema/*_pb2.py
find . -name "*.pyc" -delete
protoc --proto_path=./lbryschema/proto --python_out=./lbryschema/schema ./lbryschema/proto/*.proto
