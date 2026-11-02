# CICD-2 In Class Coding Test

## Running Service
Run the service by opening terminal in the project directory
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
once running, open the forwarded port, and append "/docs" to the end of the url to open the swagger page and test your application! (hopefully runs...)

## Testing and Coverage
an important untested section of loans logic would be to test getting a missing loan returns 404, so if a loan is removed, trying to fetch that loan would be caught instead of throwing 500*/internal errors. 

another untested section could be to test deleting loans, and to test if deleted loans return 404 as this confirms the deletion logic, as well as the fetch logic (ensuring loans can be deleted, and arent still in system afterwards)

Coverage couldnt be attained due to issues running application / creating Db