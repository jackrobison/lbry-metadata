## Protobuf schema for claims made on the lbrycrd blockchain

#### Build
There are prebuilt protobuf files in the module, so building fresh is not necessary for most. If you want to compile the protobuf files fresh, first install `protoc`

To install it on OS X, run `brew install protobuf`. Or for Ubuntu, run `sudo apt-get install protobuf-compiler python-protobuf`
 
Once protobuf is installed, run `./build.sh` to compile the .proto files.

#### Install
To install in development mode, run `pip install -r requirements.txt; pip install -e .` from the repo directory.

#### Tests
To run the tests, run `./run_tests_and_pylint.sh` from the repo directory.
