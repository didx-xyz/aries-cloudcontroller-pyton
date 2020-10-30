token=$(docker logs  aries-fl_nhstrust-notebook_1 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "NHS Trust - http://127.0.0.1:8888/?token=$token"
token=$(docker logs  aries-fl_regulator-notebook_1 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "Regulator - http://127.0.0.1:8889/?token=$token"
token=$(docker logs  aries-fl_researcher-notebook_1  2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "Researcher - http://127.0.0.1:8890/?token=$token"
token=$(docker logs  aries-fl_hospital1-notebook_1 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "Hospital1 - http://127.0.0.1:8891/?token=$token"
token=$(docker logs  aries-fl_hospital2-notebook_1 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "Hospital2 - http://127.0.0.1:8892/?token=$token"
token=$(docker logs  aries-fl_hospital3-notebook_1 2>&1 | grep "127.0.0.1):8888/" | cut -d"=" -f2 | head -1); echo "Hospital3 - http://127.0.0.1:8893/?token=$token"