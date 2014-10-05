#!/bin/sh

curl -d '{"username":"fapiko","password":"invalid"}' -H "Content-type: application/json" http://localhost:5000/session/create
