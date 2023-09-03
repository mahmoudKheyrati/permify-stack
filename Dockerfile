FROM gcr.io/distroless/static-debian11
COPY permify1 /app
CMD ["/app/permify1"]