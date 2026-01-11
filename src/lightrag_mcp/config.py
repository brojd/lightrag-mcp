"""
Configuration module for LightRAG MCP server.
"""

import argparse

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 9621
DEFAULT_API_KEY = ""
DEFAULT_SCHEME = "http"


def parse_args():
    """Parse command line arguments for LightRAG MCP server."""
    parser = argparse.ArgumentParser(description="LightRAG MCP Server")
    parser.add_argument(
        "--host", default=DEFAULT_HOST, help=f"LightRAG API host (default: {DEFAULT_HOST})"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"LightRAG API port (default: {DEFAULT_PORT})",
    )
    parser.add_argument("--api-key", default=DEFAULT_API_KEY, help="LightRAG API key (optional)")
    parser.add_argument(
        "--scheme",
        choices=["http", "https"],
        default=DEFAULT_SCHEME,
        help=f"HTTP scheme (default: {DEFAULT_SCHEME})",
    )
    parser.add_argument(
        "--no-verify-ssl",
        action="store_true",
        help="Disable SSL certificate verification for HTTPS connections",
    )
    return parser.parse_args()


args = parse_args()

LIGHTRAG_API_HOST = args.host
LIGHTRAG_API_PORT = args.port
LIGHTRAG_API_KEY = args.api_key
LIGHTRAG_API_SCHEME = args.scheme
LIGHTRAG_VERIFY_SSL = not args.no_verify_ssl
LIGHTRAG_API_BASE_URL = f"{LIGHTRAG_API_SCHEME}://{LIGHTRAG_API_HOST}:{LIGHTRAG_API_PORT}"
