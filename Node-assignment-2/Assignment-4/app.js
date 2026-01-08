const axios = require("axios");

async function fetchData() {
    try {
        console.log("fetching data....");

        // this will wait till the promise get resolved or rejected.
        const result = await new Promise((resolve, reject) => {
            setTimeout(() => {
                const success = false;

                if (success) {
                    resolve("Data Fetched successfully");
                } else {
                    reject("Data not received.");
                }
            }, 2000);
        });

        console.log(result);
        console.log("done.");
    } catch (err) {
        console.log(err);
    }
}

fetchData();

async function getPostsFirst() {
    try {
        const response = await axios.get(
            `https://jsonplaceholder.typicode.com/posts`
        );

        posts = response.data.slice(0, 5);

        posts.forEach((post, index) => {
            console.log(`\nPost ${index + 1}`);
            console.log(`Title: ${post.title}`);
            console.log(`Body: ${post.body}`);
        });
    } catch (err) {
        console.log(err);
    }
}

getPostsFirst();

// use of promise.all

async function getComments() {
    try {
        const commentsResponse = await axios.get(
            `https://jsonplaceholder.typicode.com/comments`
        );
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (commentsResponse) {
                    // console.log(commentsResponse.data.slice(0, 5));
                    resolve(commentsResponse.data.slice(0, 5));
                } else {
                    reject("Comments data fetched failed.");
                }
            }, 500);
        });
    } catch (err) {
        console.log(err);
    }
}

// getComments();

async function getPosts() {
    try {
        const postsResponse = await axios.get(
            `https://jsonplaceholder.typicode.com/posts`
        );
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (postsResponse) {
                    // console.log(postsResponse.data.slice(0, 5));
                    resolve(postsResponse.data.slice(0, 5));
                } else {
                    reject("Posts data fetched failed.");
                }
            }, 500);
        });
    } catch (err) {
        console.log(err);
    }
}
// getPosts();

async function getPostsAndComments() {
    try {
        const [posts, comments] = await Promise.all([
            getPosts(),
            getComments(),
        ]);

        console.log("Posts fetched:", posts.length);
        console.log("Comments fetched:", comments.length);
    } catch (error) {
        console.error("Error fetching data:", error.message);
    }
}

getPostsAndComments();
