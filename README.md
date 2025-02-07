# PriceFlex AI MVP

This repository contains the early prototype (MVP) for the PriceFlex AI project, a minimal dynamic pricing recommendation tool for Shopify merchants.

## Project Objectives
1. Fetch basic competitor prices (Google Shopping or direct competitor websites).
2. Compare competitor data with user-defined margins/floors.
3. Provide recommended price changes (manual approval, no full automation yet).
4. Emphasize ethical, transparent dynamic pricing (small daily shift limits).

## Folder Structure
- `/scraper/`: Python/Node scripts to pull competitor data
- `/db/`: Minimal database schema (SQL scripts or config)
- `/app/`: If building a small web UI or email-based interface
- `/docs/`: Any further design notes or architecture references

## Roadmap
- Month 1: Basic scraping & margin guardrails
- Month 2: Simple UI or daily email digest for recommended prices
- Month 3: Pilot testing with 5-10 merchants, feedback and refinements

**Note**: This MVP is strictly scope-limited to keep dev costs to ~£300/month. Advanced features like brand sentiment, B2B expansions, or HPC modules will come later.

## Contributing
- This is a personal dev project. If you’re a tester or friend with feedback, feel free to open issues or pass notes.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix/macOS
   venv\Scripts\activate     # For Windows


-- End of README --
