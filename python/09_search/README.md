## Text Search
This blog is used to understand different search algorithms and techniques.


## Content
- [How text search works](#how-text-search-works)
- [Search Index](#search-index)
  - [Text Search Optimization](#text-search-optimization)
- [Apache Lucene](#apache-lucene)
- [Elasticsearch](#elasticsearch)
  - [Characteristics](#characteristics)


## How text search works?
When you have a large database table with millions of records, searching through it can be painfully slow. Think about a table with customer information containing names, addresses, phone numbers, and other details.

Let’s say you want to find all customers whose name contains `"Smith"`. Without a search index, the database has to check every single row in the table one by one. This is called a full table scan, and it's highly inefficient.


## Search Index
A search index solves this performance problem. It's a specialized data structure that stores your data in a way that makes searching much faster. When you search for `"Smith"` in a database with a proper search index, instead of checking every row, the database uses the index to jump directly to the relevant records.

This is possible because database contains a mapping between a word or token and the records that contain that token. This is similar to how any database index works. But search indexes are specifically designed to handle text searches efficiently. They can quickly find partial matches, handle different word forms, and even account for common misspellings.

### Text Search Optimization
Unlike regular database indexes (like `B-trees` or `hash` tables used for numeric or exact matches), search indexes are optimized for text search:
- **Tokenization**: Breaking text into smaller searchable terms. For example, "John Smith" becomes ["John", "Smith"].
- **Stopword Removal**: Common words like "and," "or," or "the" are ignored to save space and improve efficiency.
- **Fuzzy Matching**: Handles partial matches (e.g., "Smit" finds "Smith") and misspellings (e.g., "Smyth" finds "Smith").



## Apache Lucene 
Apache Lucene is one of the most popular open-source search index implementations. Lucene handles all the complex work of creating and maintaining search indexes like including breaking text into searchable terms, removing common words, and storing the processed data efficiently.


## Elasticsearch
Elasticsearch, built on top of Lucene, takes these capabilities even further. It's a distributed search engine that can handle massive amounts of data across multiple servers. Many major websites and applications use Elasticsearch to power their search features. It provides a simple way to set up search functionality that can scale as your data grows, and it includes features like real-time search, automatic suggestions, and analytics capabilities.

### Characteristics
- Elasticsearch simplifies Lucene's power by wrapping it in a distributed, scalable, and user-friendly platform.
- **Distributed system**: Handles large-scale data across multiple nodes/servers.
- **Real-time search**: Enables instant search results.
- **Scalability**: Grows with your data.
- **Advanced features**: Includes auto-complete, suggestions, analytics, and more.
- **Usage**: It’s widely used in applications needing robust search capabilities (e.g., e-commerce websites, content management systems, and big data analytics).