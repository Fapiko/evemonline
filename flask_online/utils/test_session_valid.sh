#!/bin/sh

curl -d '{"username":"fapiko","password":"pwd123"}' -H "Content-type: application/json" http://localhost:5000/session/create
