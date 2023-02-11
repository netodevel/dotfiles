#### Syntax to Copy from Container to Docker Host

```docker cp {options} CONTAINER:SRC_PATH DEST_PATH```

#### Syntax to Copy from Docker Host to Container

```docker cp {options} SRC_PATH CONTAINER:DEST_PATH``` 


#### Set all container to not restart anymore
`docker update --restart=no $(docker container ls -a -q)`

