## # **CloudFront**
Edge-computing and delivering content closer to your customer's locations.

- AWS distributes your content to more than 225 edge locations & 13 regional mid-tier caches on six continents and 47 different countries

- origins define the sources where a distribution retrieves its content if it's not cached yet

- a single distribution can use multiple origins

- caching behavior is controlled by a cache policy, either AWS managed or custom (which parts of the request should be used as a cache-key)

- Lambda@Edge and CloudFront functions allow you to run general-purpose code on edge locations close to the customer

- with geo-restrictions, you can enforce approval or blocking lists for specific countries

- CloudFront supports AWS Web Application Firewall (WAF) that lets you monitor HTTP/s requests and control access to your content