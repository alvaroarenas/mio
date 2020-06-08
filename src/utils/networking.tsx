const loadJsonData = async (url: string) => {
  try {
    const response = await fetch(url);
    return await response.json();
  } catch (e) {
    console.log(`Error when fetching ${url}. ${e.message}`);
    return [];
  }
};

export default loadJsonData;
