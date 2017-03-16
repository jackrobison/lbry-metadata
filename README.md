Schema for claims made on the lbrycrd blockchain

To install, you need to have `protoc` in order to compile the .proto files. On OS X, you 
can install protobuf with `brew install protobuf`. On ubuntu install with `sudo apt-get install protobuf-compiler
 python-protobuf`
 
To compile the .proto files, run `./build.sh`, then you can install lbryschema with `pip install -r requirements.txt; pip install .`

To run the tests, use `trial tests` from the repo directory.
