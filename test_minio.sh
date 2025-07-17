curl -w "\nStatus: %{http_code}\nTime elapsed: %{time_total}s\n" -o ignore/file.png -s "http://localhost:9001/api/v1/buckets/test-public/objects/download?prefix=1.png"

curl -w "\nStatus: %{http_code}\nTime elapsed: %{time_total}s\n" -o ignore/file.mov -s "http://localhost:9001/api/v1/buckets/test-public/objects/download?prefix=v1.mov"