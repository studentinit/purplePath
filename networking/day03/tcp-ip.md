

there are many different types of networking models when it comes to the layer structure.

below is the tcp/ip vs osi models.

| osi            |     | tcp/ip        |
| -------------- | --- | ------------- |
| 7 application  |     | 4 application |
| 6 presentation |     | 4 application |
| 5 session      |     | 4 application |
| 4 transport    |     | 3 transport   |
| 3 network      |     | 2 internet    |
| 2 data link    |     | 1 link        |
| 1 physcal      |     | 1 link        |


# best model type for personal use

| layers         | who needs to worry about it(typically) |
| -------------- | -------------------------------------- |
| 7 application  | software developers                    |
| 7 presentation | software developers                    |
| 7 session      | software developers                    |
| 4 transport    | network guys                           |
| 3 network      | network guys                           |
| 2 data link    | network guys                           |
| 1 physcal      | network guys                           |


---
using tcp/ip model, below is a diagram demonstrating the process of data being sent from host a to host b through 2 routers




| A           |       |        | router   |                     | router   |       |       | B           |
| ----------- | ----- | ------ | -------- | ------------------- | -------- | ----- | ----- | ----------- |
|             |       |        |          |                     |          |       |       |             |
| application |       | <-<-<  | -------  | process-to-process  | -------  | ->->> |       | application |
| v           |       |        |          |                     |          |       |       |             |
| transport   |       | <-<-<  | -------  | host-to-host        | -------  | ->->> |       | transport   |
| v           |       |        |          |                     |          |       |       |             |
| internet    |       | -----> | internet |                     | internet |       |       | internet    |
| v           |       | ^      |          | v"            "^    | ^        | v     |       |             |
| link        |       | ^      | link     | v"            "^    | link     | v     |       | link        |
| v           |       | ^      |          | v"            "^    | ^        | v     |       |             |
| >->->->     | ->->- | eth    |          | fiber, satalite etc |          | eth   | ->->- | >->->->     |
