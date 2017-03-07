find . -name \*.pyc -delete
rm -rf ./lbryschema/schema/*_pb2.py
protoc --proto_path=./lbryschema/proto --python_out=./lbryschema/schema ./lbryschema/proto/*.proto
