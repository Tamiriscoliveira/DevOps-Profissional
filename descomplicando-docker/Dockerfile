FROM golang:1.19 as buildando
WORKDIR /app
COPY  . ./
RUN go mod init hello
RUN go build -o /app/hello

FROM  alpine:3.15.9
COPY  --from=buildando /app/hello /app/hello
ENV  APP="hello_world"
ARG  TERAPIA="correr" 
RUN echo "A minha terapia é: $TERAPIA"
CMD ["/app/hello"]
