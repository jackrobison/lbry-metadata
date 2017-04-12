## Protobuf schema for [LBRY](https://github.com/lbryio/lbry) claims and spec for lbry:// URIs

lbryschema is a [protobuf](https://github.com/google/protobuf) schema that defines claims are structured and validated in the LBRY blockchain. 
There is also code to construct, parse, and validate lbry:// URIs.  

### Use

Add `git+https://github.com/lbryio/lbryschema.git#egg=lbryschema` to `requirements.txt`

### Protobuf Schema

See [docs/schema.md](https://github.com/lbryio/lbryschema/blob/master/docs/schema.md).

### Development

To install in development mode, run `pip install -r requirements.txt; pip install -e .` from the repo directory.

To run the tests, run `./run_tests_and_pylint.sh` from the repo directory.

#### Compile .proto files

There are compiled protobuf files in `lbryschema/schema` (see the files that end in `_pb2.py`), so compiling fresh is not necessary for most.   

If you want to compile the protobuf files yourself, install `protoc`:

- macOS: `brew install protobuf`
- Ubuntu: `sudo apt-get install protobuf-compiler python-protobuf`
 
Once protobuf is installed, run `./build.sh` to compile the .proto files.

