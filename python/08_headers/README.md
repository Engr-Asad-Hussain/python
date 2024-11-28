## Headers
This section contains different headers and their use cases.

### Sec-CH-UA-Mobile
The "Sec-CH-UA-Mobile" header is a HTTP header that tells a web server whether the user's browser is currently running on a mobile device, essentially indicating if the user is accessing the website from a phone or tablet as opposed to a desktop computer; it's considered a "client hint" which allows servers to optimize content delivery based on the device type. 

- It sends a simple "`true`" or "`false`" signal to the server, where "true" means the browser is on a mobile device. 
- The header value is usually expressed as "`?1`" for a mobile device and "`?0`" for a desktop device. 
- This information allows websites to serve different versions of their content optimized for mobile screens if needed.


### Sec-CH-UA-Platform
The "Sec-CH-UA-Platform" header is a user agent client hint that indicates the operating system or platform on which the browser is running, essentially telling the server what type of device the user is using, like "Windows", "Android", "macOS", or "Linux" - providing information without revealing too much detailed user data. 

- This header is part of the "`User-Agent Client Hints`" specification, which aims to provide more granular device information to servers while protecting user privacy by not sending overly specific details. 
- This means that the information provided is considered less sensitive compared to a full user-agent string. 
- If a user is browsing on a Windows computer, the "Sec-CH-UA-Platform" header might be set to "`Windows`". 
