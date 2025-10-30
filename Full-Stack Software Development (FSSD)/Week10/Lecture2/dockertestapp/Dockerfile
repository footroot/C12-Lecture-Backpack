# Use the official Node.js image
FROM node:23-alpine
    
# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependancy
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose the port our application will be running 
EXPOSE 5173

# Start the application
CMD ["npm", "run", "dev"]