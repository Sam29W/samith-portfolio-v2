#!/usr/bin/env python3
"""
Portfolio Website Runner
A simple script to run the Flask application
"""

import os
import sys
from app import app

def main():
    """Main function to run the Flask application"""
    try:
        print("Starting Samith's Portfolio Website...")
        print("Backend: Flask (Python)")
        print("Frontend: HTML, CSS, JavaScript")
        print("\n" + "="*50)
        print("🌐 Server starting on http://localhost:5000")
        print("📊 API available at http://localhost:5000/api/")
        print("💬 Contact form: http://localhost:5000/api/contact")
        print("📈 Health check: http://localhost:5000/api/health")
        print("="*50 + "\n")
        
        # Run the Flask app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
        
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()