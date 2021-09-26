    import AWS from 'aws-sdk';
    import S3 from 'aws-s3';
    // Initialize the Amazon Cognito credentials provider
    AWS.config.region = 'us-east-2'; // Region
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-east-2:3698e615-3abb-4f54-8e7b-8d0d43af3eaa',
    });

    https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#putObject-property
    /* The following example uploads an object. The request specifies optional object tags. The bucket is versioned, therefore S3 returns version ID of the newly created object. */

    var params = {
        Body: <Binary String>, 
        Bucket: "examplebucket", 
        Key: "HappyFace.jpg"
   };
   s3.putObject(params, function(err, data) {
     if (err) console.log(err, err.stack); // an error occurred
     else     console.log(data);           // successful response
     /*
     data = {
      ETag: "\"6805f2cfc46c0f04559748bb039d69ae\"", 
      VersionId: "psM2sYY4.o1501dSx8wMvnkOzSBB.V4a"
     }
     */
   });