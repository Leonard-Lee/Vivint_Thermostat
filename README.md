# Vivint Smart Home Thermostat Web API

* [Goal](#goal)
* [RESTful URLs](#restful-urls)
* [HTTP Verbs](#http-verbs)
* [Error handling](#error-handling)


## Goal

The goal aim to support truly RESTful Web API for Vivint Smart Home Thermostat.

## RESTful URLs

### General guidelines for RESTful URLs
* A URL identifies a resource.
* URLs should include nouns, not verbs.
* Use HTTP verbs (GET, POST, PUT, DELETE) to operate on thermostat.
* Web API results are in JSON format.

### URL examples
* List of thermostat:
    * GET http://www.example.com/thermostat
* A single thermostat in JSON format:
    * GET http://www.example.com/thermostat/33


## HTTP Verbs

Here's an example of how HTTP verbs map to create, read, update, delete operations for Vivint Smart Home Thermostat:

| HTTP METHOD   | POST                    | GET                       | PUT                                 | DELETE                          |
| --------------| ------------------------| --------------------------| ------------------------------------| --------------------------------|
| CRUD OP       | CREATE                  | READ                      | UPDATE                              | DELETE                          |
| /thermostat   | Create a new thermostat | List all thermostats      | Bulk update                         | Delete all thermostats          |
| /thermostat/3 | Error                   | Show the 3rd thermostat   | If exists, update the 3rd thermostat| Delete the 3rd thermostat|

## Error handling

Error responses should include a common HTTP status code, message for the developer, message for the end-user (when appropriate), internal error code (corresponding to some specific internally determined ID), links where developers can find more info. For example:

    {
      "status" : 400,
      "result" : "Sorry, the item you were searching or updating was not found."
    }

Use three simple, response HTTP codes indicating: success, failure of client-side problem, and failure of server-side problem:
* 200 - OK
* 400 - Bad Request
* 404 - Not Found
* 500 - Internal Server Error