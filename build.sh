cd build
find . \! -name '.gitkeep' -delete
cd ../

NESTML_INSTALL_DIR="${NESTML_INSTALL_DIR:-../../3rdparty/nestml/target}"
java -jar "$NESTML_INSTALL_DIR"/nestml.jar research_team_models/ --target build/

cd build
cmake -Dwith-nest=$NEST_INSTALL_DIR/bin/nest-config .
make all
make install

