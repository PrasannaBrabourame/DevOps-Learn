const AWS = require("aws-sdk");
const region = '**** REGION ****';
const sns = new AWS.SNS({ region });
const params = {
  PlatformApplicationArn: "****Platform Application ARN***",
  Token: '**** Andriod or IOS Device Token'
};

sns.createPlatformEndpoint(params, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log("Successfully created platform endpoint");
});