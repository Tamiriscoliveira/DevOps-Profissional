FROM nginx:1.21.4 as buildando
LABEL maintainer="tamiriscoutinho@gmail.com"
COPY index.html /usr/share/nginx/html/
FROM alpine:3.15.9
RUN apk add --no-cache nginx 
COPY --from=buildando  /usr/share/nginx/html/ /usr/share/nginx/html/
EXPOSE 80
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
HEALTHCHECK --timeout=2s CMD curl -f localhost || exit 1









