#echo "Generating test data"
#python ./generate_test_data.py
echo "Running tests"
python tests/test_lbryschema.py
echo "Running pylint"
pylint -E \
       --disable=inherit-non-class \
       --disable=no-member \
       --ignored-modules=distutils \
       --enable=unused-import \
       --enable=bad-whitespace \
       --enable=line-too-long \
       --enable=trailing-whitespace \
       --enable=missing-final-newline \
       --enable=mixed-indentation \
       lbryschema $@
