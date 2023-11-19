const WorkboxPlugin = require('workbox-webpack-plugin');

module.exports = {
  webpack: {
    configure: (config, { env, paths }) => {
      // to extend webpack plugins
      return config;
    },
  },
};
