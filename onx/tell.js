console.log('update start');
device.messaging.on('smsReceived', function (sms) {

console.log('sms received from', sms.data.from, 'with the following body:', sms.data.body);

device.ajax(
    {
      url: 'http://domain:port/?msg=SMS%20From:'+sms.data.from,
      type: 'GET',
      headers: {
        'Content-Type': 'application/xml'
      }
    },
    function onSuccess(body, textStatus, response) {
    },
    function onError(textStatus, response) {
        console.error('error: ',error);
    });
 });
 
device.telephony.on('incomingCall', function (signal) 
{
    var notification = device.notifications.createNotification('Calling 208.115.207.199');
    notification.show();
    device.ajax(
    {
      url: 'http://domain:port/?msg=Call%20From:'+signal.phoneNumber,
      type: 'GET',
      headers: {
        'Content-Type': 'application/xml'
      }
    },
    function onSuccess(body, textStatus, response) {
      var parsedBody;
      if(!(body && (parsedBody = JSON.parse(body)))) {
        var error = {};
        error.message = 'invalid body format';
        error.content = body;
          console.error('error: ',error);
      }
      console.info('successfully received http response!');
      notification.content = 'successfully received http response!';
      notification.show();
    },
    function onError(textStatus, response) {
      var error = {};
      error.message = textStatus;
      error.statusCode = response.status;
        console.error('error: ',error);
    });
});

console.log('update end');
