mkdir -p ~/.tt
cp -r tt/* ~/.tt/
py_bin=`which python3`
shebang="#!$py_bin"
exec 3<> ~/.tt/main.py && awk -v TEXT="$shebang" 'BEGIN {print TEXT}{print}' ~/.tt/main.py >&3
echo "Successfully installed tt. Config and app is in ~/tt/ directory."

