[[py]]
# FILE + IO ERRORS:
___

| filenotfounderror | - the file you are trying to access does not exist             |
| ----------------- | -------------------------------------------------------------- |
| permissionerror   | - do not have permission to access file or folder              |
| isAdirectoryerror | - tried to open a folder as if it was a file                   |
| ioerror           | - general input/output problem(file cannot be read or written) |

# DATA + VALUE ERRORS:
___

| valueerror     | - data has the right type but wrong value(cannot convert "cat" to int)       |
| -------------- | ---------------------------------------------------------------------------- |
| typeerror      | - wrong type of object used(str + int)                                       |
| keyerror       | - trying to access a dict key that does not exist                            |
| indexerror     | - list index is out of range(ls = 5 items but you tried accessing item nr 7) |
| attributeerror | - object does not have the capability you're trying use                      |

# SECURITY ERROR:
___

| importerror         | - module you are trying to import cannot be found(importand  when loading security / AI tools) |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| modulenotfounderror | - newer version of importerror for py( module truly not instaled)                              |
| connectionerror     | - network connection failed(scanning servers, APIs)                                            |
| timeouterror        | - an operation took too long to complete(scanning)                                             |
| permissionerror     | - (repeat here)file/sys changes in sec scripts                                                 |

# MATH, AI/ML + DATASCIENCE ERRORS:
___

| zerodevisionerror | - tried to divide num by zero(can break ai calculations)   |
| ----------------- | ---------------------------------------------------------- |
| overflowerror     | - num = too big to handle(rare but possible)               |
| memoryerror       | - ran out of memory(important when training big ai models) |

# CATCH-ALL:
___

| exception    | - base for all errors == lazy safetynet               |
| ------------ | ---------------------------------------------------- |
| runtimeerror - something went wrong that is not easily classified ed |
