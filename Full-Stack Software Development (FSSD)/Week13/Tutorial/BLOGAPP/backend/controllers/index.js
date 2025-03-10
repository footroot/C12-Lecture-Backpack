const getHomePage = (req, res) => {
  res.json({
    message: "A new message",
  });
};

const getBlogs = (req, res) => {
  res.json([
    {
      author: "Dan Walobwa",
      title: "Harry Potter",
    },
    {
      author: "Bongani Gumbo",
      title: "Percy Jackson",
    },
    {
      author: "Jane Doe",
      title: "Livestorm",
    },
  ]);
};

export { getHomePage, getBlogs };
