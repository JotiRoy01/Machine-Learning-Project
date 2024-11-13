for dir in exception logger pipeline component config entity
do
    echo [$(date)]: "Creating", housing/$dir
    mkdir -p housing/$dir
    echo [$(date)]: "Creating __init__.py inside above folder"
    touch housing/$dir/"__init__.py"
done