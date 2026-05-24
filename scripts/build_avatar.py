# import os
# import sys
# import base64
# from PIL import Image

# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python build_avatar.py <source_image_path> <output_svg_path>")
#         sys.exit(1)
        
#     src_path = sys.argv[1]
#     out_svg_path = sys.argv[2]
    
#     if not os.path.exists(src_path):
#         print(f"Error: Source image {src_path} not found.")
#         sys.exit(1)
        
#     out_dir = os.path.dirname(out_svg_path)
#     if out_dir and not os.path.exists(out_dir):
#         os.makedirs(out_dir)
        
#     print(f"Opening image: {src_path}")
#     img = Image.open(src_path)
    
#     # Crop to square center
#     w, h = img.size
#     min_dim = min(w, h)
#     left = (w - min_dim) / 2
#     top = (h - min_dim) / 2
#     right = (w + min_dim) / 2
#     bottom = (h + min_dim) / 2
#     img = img.crop((left, top, right, bottom))
    
#     # Resize to 300x300
#     img = img.resize((300, 300), Image.Resampling.LANCZOS)
    
#     # Compress and save to buffer as PNG
#     import io
#     buf = io.BytesIO()
#     img.save(buf, format="PNG", optimize=True)
#     b64_data = base64.b64encode(buf.getvalue()).decode("utf-8")
    
#     # SVG Template
#     svg_template = f"""<svg width="220" height="220" viewBox="0 0 220 220" fill="none" xmlns="http://www.w3.org/2000/svg">
#   <defs>
#     <!-- Purple neon glow filter -->
#     <filter id="purple-glow" x="-20%" y="-20%" width="140%" height="140%">
#       <feGaussianBlur stdDeviation="6" result="blur" />
#       <feMerge>
#         <feMergeNode in="blur" />
#         <feMergeNode in="SourceGraphic" />
#       </feMerge>
#     </filter>
#     <!-- Red neon glow filter -->
#     <filter id="red-glow" x="-20%" y="-20%" width="140%" height="140%">
#       <feGaussianBlur stdDeviation="4" result="blur" />
#       <feMerge>
#         <feMergeNode in="blur" />
#         <feMergeNode in="SourceGraphic" />
#       </feMerge>
#     </filter>
#     <!-- Clip path for circle -->
#     <clipPath id="circle-clip">
#       <circle cx="110" cy="110" r="90" />
#     </clipPath>
#   </defs>

#   <!-- Glowing outer purple ring -->
#   <circle cx="110" cy="110" r="94" stroke="#7a00ff" stroke-width="4" stroke-dasharray="10 5 5 5" fill="none" filter="url(#purple-glow)" opacity="0.8">
#     <animateTransform attributeName="transform" type="rotate" from="0 110 110" to="360 110 110" dur="20s" repeatCount="indefinite"/>
#   </circle>

#   <!-- Glowing inner red ring -->
#   <circle cx="110" cy="110" r="90" stroke="#ff003c" stroke-width="2" fill="none" filter="url(#red-glow)" />

#   <!-- Technical crosshairs and tick marks for cyberpunk feel -->
#   <line x1="110" y1="5" x2="110" y2="12" stroke="#ff003c" stroke-width="2" />
#   <line x1="110" y1="208" x2="110" y2="215" stroke="#ff003c" stroke-width="2" />
#   <line x1="5" y1="110" x2="12" y2="110" stroke="#ff003c" stroke-width="2" />
#   <line x1="208" y1="110" x2="215" y2="110" stroke="#ff003c" stroke-width="2" />

#   <!-- Avatar image clipped to circle -->
#   <g clip-path="url(#circle-clip)">
#     <image href="data:image/png;base64,{b64_data}" x="20" y="20" width="180" height="180" />
#   </g>
# </svg>
# """

#     with open(out_svg_path, "w", encoding="utf-8") as f:
#         f.write(svg_template)
        
#     print(f"Successfully generated glowing avatar at {out_svg_path}!")

# if __name__ == "__main__":
#     main()
