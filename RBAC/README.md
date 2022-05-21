# Security

### Teams

The project is divided by Teams by each microservice!

### Secrets

The keys and certificates for each Team are saved on the Google Cloud Platform.  
Using the: Security - Secret Manager

You need to have the following secrets eg:  
adminoperations-cert  
adminoperations-key	  

If you are a new member of the team just ask for the Admin to give you the permissions to access the secrets!

If is your project:

You can generate them with: 

```
openssl genrsa -out adminOperationsTeam.key 2048
openssl req -new -key adminOperationsTeam.key -out adminOperationsTeam.csr -subj "/CN=adminOperationsTeam/O=adminOperationsTeam"
```

The keys are saved on the Team Folder.  
To get the geys you can run:

```
gcloud secrets versions access 1 --secret="usermanagement-key" --format='get(payload.data)' | tr '_-' '/+' | base64 -d > userManagement.key
```

## Resources

All the resources are listed on the Roles yaml they are defined to give only permissions to create/list/update

