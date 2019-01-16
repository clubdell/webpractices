FROM node:8-alpine AS builder

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:8-alpine

COPY --from=builder /app /app
COPY . .

EXPOSE 3000
CMD npm start
