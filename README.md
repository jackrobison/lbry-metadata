## Protobuf schema for claims made on the lbrycrd blockchain

To install, you first need compile the protobuf files with `protoc`. On OS X, you 
can install protoc with `brew install protobuf`. On ubuntu install with `sudo apt-get install protobuf-compiler python-protobuf`
 
Once protobuf is installed, run `./build.sh` to compile the .proto files. Then you can install lbryschema with `pip install -r requirements.txt; pip install .`

To run the tests, use `trial tests` from the repo directory.
