### AWS Lambda Examples

- Hello World example without API Gateway
```bash
sam build
sam local invoke HelloWorldFunction -e events/event.json
```
- Hello World example with API Gateway
```bash
sam local start-api
```

> Must use event path specified on template.yaml (hello)

```bash
curl https://127.0.0.1:3000/hello
```
- Customs Example
