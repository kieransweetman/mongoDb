FROM  alpine/mongosh

ARG MONGODB_INITDB_ROOT_USERNAME_FILE
ARG MONGODB_INITDB_ROOT_PASSWORD_FILE

# Use the arguments as environment variables
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}


RUN apk update 

COPY init-mongo.js /docker-entrypoint-initdb.d/

# Start the shell and connect to the MongoDB server
# Run the initialization script and keep the container running
CMD ["sh", "-c", "mongosh \"mongodb://${MONGO_INITDB_ROOT_USERNAME}:${MONGO_INITDB_ROOT_PASSWORD}@mongodb:27017/admin\" /docker-entrypoint-initdb.d/init-mongo.js && while :; do sleep 1; done"]