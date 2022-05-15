import axios from 'axios';

const api = axios.create({
    baseURL: 'https://dog.ceo/api/breeds/image/random'
});

export default api;
