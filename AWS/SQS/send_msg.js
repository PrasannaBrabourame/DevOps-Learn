const AWS = require('aws-sdk');

// Set the region and your AWS credentials
AWS.config.update({
  region: 'your-region',
  accessKeyId: 'your-access-key-id',
  secretAccessKey: 'your-secret-access-key',
});

// Create an SQS service object
const sqs = new AWS.SQS();

// Define the parameters for sending the message
const params = {
  MessageBody: 'Hello from JavaScript!', // Message content
  QueueUrl: 'your-queue-url', // URL of the SQS queue
};

// Send the message to the SQS queue
sqs.sendMessage(params, (err, data) => {
  if (err) {
    console.log('Error sending message:', err);
  } else {
    console.log('Message sent:', data.MessageId);
  }
});
