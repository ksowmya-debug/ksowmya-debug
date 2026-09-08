import os
import base64

assets_dir = r"C:\Users\krish\OneDrive\Desktop\ksowmya-debug\assets"

avatar_path = os.path.join(assets_dir, "avatar.png")
if os.path.exists(avatar_path):
    with open(avatar_path, "rb") as f:
        avatar_b64 = base64.b64encode(f.read()).decode("utf-8")
else:
    avatar_b64 = ""

# NEW CUTE PALETTE
# Bg: #0f0c1b, #151028, #1c1535 (Soft dark violet/midnight)
# Glows: #ec4899 (Pink), #d946ef (Fuchsia), #a855f7 (Purple)
# Code Bg: #130e24, #1a1430
# Borders: #2a1f4c

hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 230" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f0c1b" />
      <stop offset="50%" stop-color="#151028" />
      <stop offset="100%" stop-color="#1c1535" />
    </linearGradient>
    <linearGradient id="border-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#d946ef" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ec4899" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="avatar-ring" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#d946ef" />
      <stop offset="100%" stop-color="#ff7eb3" />
    </linearGradient>
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f472b6" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <radialGradient id="p-glow" cx="28%" cy="50%" r="35%">
      <stop offset="0%" stop-color="#d946ef" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#d946ef" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="b-glow" cx="85%" cy="35%" r="40%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0" />
    </radialGradient>
    <filter id="glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <clipPath id="avatar-clip">
      <circle cx="285" cy="115" r="56" />
    </clipPath>
  </defs>

  <!-- Card Background -->
  <rect x="2" y="2" width="936" height="226" rx="22" fill="url(#bg-grad)" stroke="url(#border-glow)" stroke-width="1.8" />
  <rect x="2" y="2" width="936" height="226" rx="22" fill="url(#p-glow)" />
  <rect x="2" y="2" width="936" height="226" rx="22" fill="url(#b-glow)" />

  <!-- Left Side: Hand-drawn doodle text -->
  <g opacity="0.9" transform="translate(36, 48)">
    <text x="32" y="32" font-family="'Segoe Print', 'Caveat', 'Comic Sans MS', cursive, sans-serif" font-size="24" font-weight="bold" fill="#fbcfe8" transform="rotate(-9 32 32)">Better</text>
    <text x="38" y="58" font-family="'Segoe Print', 'Caveat', 'Comic Sans MS', cursive, sans-serif" font-size="21" font-weight="bold" fill="#fce7f3" transform="rotate(-6 38 58)">+ Code</text>
    <text x="44" y="90" font-family="'Segoe Print', 'Caveat', 'Comic Sans MS', cursive, sans-serif" font-size="26" font-weight="bold" fill="#fdf2f8" transform="rotate(-8 44 90)">Bigger</text>
    <text x="50" y="120" font-family="'Segoe Print', 'Caveat', 'Comic Sans MS', cursive, sans-serif" font-size="26" font-weight="bold" fill="#fbcfe8" transform="rotate(-5 50 120)">Dreams</text>
    <!-- Little Pink Heart -->
    <path d="M148 118 C148 112, 142 107, 136 110 C130 107, 124 112, 124 118 C124 125, 136 132, 136 132 C136 132, 148 125, 148 118 Z" fill="#ec4899" opacity="0.9" filter="url(#glow-filter)" />
  </g>

  <!-- Avatar Glowing Ring -->
  <circle cx="285" cy="115" r="61" fill="none" stroke="url(#avatar-ring)" stroke-width="3.5" filter="url(#glow-filter)" />
  <circle cx="285" cy="115" r="59" fill="none" stroke="url(#avatar-ring)" stroke-width="2.5" />

  <!-- Avatar Image -->
  <image href="data:image/png;base64,{avatar_b64}" x="229" y="59" width="112" height="112" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />

  <!-- Center Content -->
  <g transform="translate(378, 74)">
    <text x="0" y="28" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="34" font-weight="700" fill="#f8fafc">
      Hi, I'm <tspan fill="url(#name-grad)" font-weight="800">Sowmya</tspan>
    </text>
    <text x="0" y="62" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="15" font-weight="500" fill="#e2e8f0">
      Full Stack Developer  <tspan fill="#ec4899">|</tspan>  <tspan fill="#a78bfa">Java</tspan>  <tspan fill="#c084fc">•</tspan>  <tspan fill="#a78bfa">Spring Boot</tspan>  <tspan fill="#c084fc">•</tspan>  <tspan fill="#a78bfa">React</tspan>  <tspan fill="#c084fc">•</tspan>  <tspan fill="#a78bfa">Cloud</tspan>
    </text>
    <text x="0" y="94" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="14.5" font-style="italic" fill="#fbcfe8">
      “Turning ideas into real-world applications” <tspan font-style="normal">✨</tspan>
    </text>
  </g>

  <!-- Right Side: Laptop Line Art Illustration -->
  <g opacity="0.8" transform="translate(785, 46)">
    <!-- Code symbol </> -->
    <text x="56" y="32" font-family="'Fira Code', 'Courier New', monospace" font-size="22" font-weight="bold" fill="#f472b6">&lt;/&gt;</text>
    
    <!-- Laptop screen -->
    <rect x="15" y="42" width="78" height="52" rx="6" fill="none" stroke="#d946ef" stroke-width="2" transform="rotate(-10 50 65)" />
    <line x1="22" y1="52" x2="34" y2="50" stroke="#f472b6" stroke-width="1.5" transform="rotate(-10 50 65)" />
    <line x1="22" y1="60" x2="60" y2="53" stroke="#a78bfa" stroke-width="1.5" transform="rotate(-10 50 65)" />
    <line x1="22" y1="68" x2="50" y2="63" stroke="#a78bfa" stroke-width="1.5" transform="rotate(-10 50 65)" />
    
    <!-- Laptop base -->
    <path d="M2 95 L98 78 L94 85 L6 102 Z" fill="none" stroke="#d946ef" stroke-width="2" />

    <!-- Cute small heart -->
    <path d="M92 48 C92 44, 88 40, 83 42 C79 40, 75 44, 75 48 C75 54, 83 59, 83 59 C83 59, 92 54, 92 48 Z" fill="none" stroke="#ff7eb3" stroke-width="1.5" />
  </g>
</svg>'''

with open(os.path.join(assets_dir, "hero-banner.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)

about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 400" width="100%" height="100%">
  <style>
    @media (prefers-color-scheme: light) {
      .text-primary { fill: #0f172a !important; }
      .text-secondary { fill: #475569 !important; }
    }
  </style>
  <defs>
    <linearGradient id="code-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110d1e" />
      <stop offset="100%" stop-color="#16112a" />
    </linearGradient>
    <linearGradient id="border-subtle" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3d2e70" />
      <stop offset="50%" stop-color="#4c3a8c" />
      <stop offset="100%" stop-color="#3d2e70" />
    </linearGradient>
  </defs>

  <!-- Left: Code Editor Card -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="556" height="394" rx="16" fill="url(#code-bg)" stroke="url(#border-subtle)" stroke-width="1.5" />
    
    <rect x="2" y="2" width="556" height="36" rx="16" fill="#1c1535" />
    <rect x="2" y="22" width="556" height="16" fill="#1c1535" />
    <line x1="2" y1="38" x2="558" y2="38" stroke="#3d2e70" stroke-width="1" />
    
    <circle cx="20" cy="20" r="5.5" fill="#ef4444" />
    <circle cx="38" cy="20" r="5.5" fill="#f59e0b" />
    <circle cx="56" cy="20" r="5.5" fill="#10b981" />
    <text x="280" y="24" font-family="'Fira Code', monospace, sans-serif" font-size="12" fill="#a78bfa" text-anchor="middle">sowmya.js</text>

    <!-- Code Content -->
    <g transform="translate(18, 62)" font-family="'Fira Code', 'Consolas', monospace" font-size="12.5" line-height="22">
      <!-- Line Numbers -->
      <g fill="#6d5c9c" text-anchor="end">
        <text x="18" y="0">1</text>
        <text x="18" y="22">2</text>
        <text x="18" y="44">3</text>
        <text x="18" y="66">4</text>
        <text x="18" y="88">5</text>
        <text x="18" y="110">6</text>
        <text x="18" y="132">7</text>
        <text x="18" y="154">8</text>
        <text x="18" y="176">9</text>
        <text x="18" y="198">10</text>
        <text x="18" y="220">11</text>
        <text x="18" y="242">12</text>
        <text x="18" y="264">13</text>
        <text x="18" y="286">14</text>
      </g>

      <!-- Code Text -->
      <g transform="translate(32, 0)">
        <text x="0" y="0"><tspan fill="#f472b6">const</tspan> <tspan fill="#a78bfa">sowmya</tspan> <tspan fill="#e2e8f0">=</tspan> <tspan fill="#fde047">{</tspan></text>
        <text x="16" y="22"><tspan fill="#a78bfa">role</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#86efac">"Full Stack Developer"</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="16" y="44"><tspan fill="#a78bfa">location</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#86efac">"India 🇮🇳"</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="16" y="66"><tspan fill="#a78bfa">currentlyBuilding</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#fde047">[</tspan></text>
        <text x="32" y="88"><tspan fill="#86efac">"Spring Boot Applications"</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="32" y="110"><tspan fill="#86efac">"Cloud &amp; DevOps Projects"</tspan></text>
        <text x="16" y="132"><tspan fill="#fde047">]</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="16" y="154"><tspan fill="#a78bfa">learning</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#fde047">[</tspan></text>
        <text x="32" y="176"><tspan fill="#86efac">"Java &amp; Spring Boot"</tspan><tspan fill="#e2e8f0">, </tspan><tspan fill="#86efac">"DSA"</tspan><tspan fill="#e2e8f0">, </tspan><tspan fill="#86efac">"AWS"</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="32" y="198"><tspan fill="#86efac">"Docker &amp; Kubernetes"</tspan></text>
        <text x="16" y="220"><tspan fill="#fde047">]</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="16" y="242"><tspan fill="#a78bfa">interests</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#fde047">[</tspan><tspan fill="#86efac">"Problem Solving"</tspan><tspan fill="#e2e8f0">, </tspan><tspan fill="#86efac">"Projects"</tspan><tspan fill="#e2e8f0">, </tspan><tspan fill="#86efac">"Music"</tspan><tspan fill="#e2e8f0">, </tspan><tspan fill="#86efac">"Anime"</tspan><tspan fill="#fde047">]</tspan><tspan fill="#e2e8f0">,</tspan></text>
        <text x="16" y="264"><tspan fill="#a78bfa">motto</tspan><tspan fill="#e2e8f0">:</tspan> <tspan fill="#86efac">"Keep Learning, Keep Growing 🚀"</tspan></text>
        <text x="0" y="286"><tspan fill="#fde047">}</tspan><tspan fill="#e2e8f0">;</tspan></text>
      </g>
    </g>
  </g>

  <!-- Right: Highlights Profile Section -->
  <g transform="translate(580, 0)">
    <g transform="translate(0, 20)">
      <circle cx="24" cy="24" r="22" fill="#1c1535" stroke="#a855f7" stroke-width="1.5" />
      <text x="24" y="30" font-size="18" text-anchor="middle">🎓</text>
      <g transform="translate(60, 16)">
        <text x="0" y="4" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" class="text-primary" fill="#f8fafc">BCA Student</text>
        <text x="0" y="24" font-family="'Segoe UI', sans-serif" font-size="13" class="text-secondary" fill="#a78bfa">From Hyderabad, India 📍</text>
      </g>
    </g>
    <g transform="translate(0, 110)">
      <circle cx="24" cy="24" r="22" fill="#1c1535" stroke="#ec4899" stroke-width="1.5" />
      <text x="24" y="30" font-size="18" text-anchor="middle">🎯</text>
      <g transform="translate(60, 14)">
        <text x="0" y="4" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" class="text-primary" fill="#f8fafc">Passionate about</text>
        <text x="0" y="23" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">Full Stack Development, DevOps,</text>
        <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">DSA &amp; Cloud Technologies</text>
      </g>
    </g>
    <g transform="translate(0, 205)">
      <circle cx="24" cy="24" r="22" fill="#1c1535" stroke="#f472b6" stroke-width="1.5" />
      <text x="24" y="30" font-size="18" text-anchor="middle">💜</text>
      <g transform="translate(60, 14)">
        <text x="0" y="4" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" class="text-primary" fill="#f8fafc">I love</text>
        <text x="0" y="23" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">Solving problems, building projects,</text>
        <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">listening to music and exploring tech.</text>
      </g>
    </g>
    <g transform="translate(0, 300)">
      <circle cx="24" cy="24" r="22" fill="#1c1535" stroke="#10b981" stroke-width="1.5" />
      <text x="24" y="30" font-size="18" text-anchor="middle">🌱</text>
      <g transform="translate(60, 14)">
        <text x="0" y="4" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" class="text-primary" fill="#f8fafc">Currently Focusing On</text>
        <text x="0" y="23" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">Java, Spring Boot, React, AWS,</text>
        <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-size="12.5" class="text-secondary" fill="#a78bfa">Docker, Kubernetes &amp; DSA</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "about-card.svg"), "w", encoding="utf-8") as f:
    f.write(about_svg)

tech_row1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 160" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110d1e" />
      <stop offset="100%" stop-color="#16112a" />
    </linearGradient>
  </defs>

  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="296" height="154" rx="16" fill="url(#card-bg)" stroke="#3d2e70" stroke-width="1.5" />
    <text x="18" y="32" font-size="16">🎨</text>
    <text x="44" y="32" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Frontend Craft</text>
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="60" height="28" rx="8" fill="#ec4899" />
      <text x="30" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">React</text>
      <rect x="68" y="0" width="90" height="28" rx="8" fill="#facc15" />
      <text x="113" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">JavaScript</text>
      <rect x="166" y="0" width="62" height="28" rx="8" fill="#ea580c" />
      <text x="197" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">HTML5</text>
      <rect x="236" y="0" width="50" height="28" rx="8" fill="#3b82f6" />
      <text x="261" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">CSS3</text>
    </g>
    <g transform="translate(16, 92)">
      <rect x="0" y="0" width="96" height="28" rx="8" fill="#0d9488" />
      <text x="48" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Tailwind CSS</text>
      <rect x="104" y="0" width="84" height="28" rx="8" fill="#a855f7" />
      <text x="146" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Bootstrap</text>
    </g>
  </g>

  <g transform="translate(315, 0)">
    <rect x="2" y="2" width="306" height="154" rx="16" fill="url(#card-bg)" stroke="#3d2e70" stroke-width="1.5" />
    <text x="18" y="32" font-size="16">🖳</text>
    <text x="44" y="32" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Backend Engineering</text>
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="58" height="28" rx="8" fill="#f97316" />
      <text x="29" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">Java</text>
      <rect x="66" y="0" width="92" height="28" rx="8" fill="#10b981" />
      <text x="112" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">Spring Boot</text>
      <rect x="166" y="0" width="66" height="28" rx="8" fill="#15803d" />
      <text x="199" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Node.js</text>
    </g>
    <g transform="translate(16, 92)">
      <rect x="0" y="0" width="84" height="28" rx="8" fill="#4c3a8c" />
      <text x="42" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Express.js</text>
      <rect x="92" y="0" width="80" height="28" rx="8" fill="#8b5cf6" />
      <text x="132" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">REST APIs</text>
      <rect x="180" y="0" width="50" height="28" rx="8" fill="#6d5c9c" />
      <text x="205" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">JWT</text>
    </g>
  </g>

  <g transform="translate(640, 0)">
    <rect x="2" y="2" width="296" height="154" rx="16" fill="url(#card-bg)" stroke="#3d2e70" stroke-width="1.5" />
    <text x="18" y="32" font-size="16">🗄️</text>
    <text x="44" y="32" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Data &amp; Cloud</text>
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="88" height="28" rx="8" fill="#0ea5e9" />
      <text x="44" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">PostgreSQL</text>
      <rect x="96" y="0" width="80" height="28" rx="8" fill="#22c55e" />
      <text x="136" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">MongoDB</text>
      <rect x="184" y="0" width="64" height="28" rx="8" fill="#3b82f6" />
      <text x="216" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">MySQL</text>
    </g>
    <g transform="translate(16, 92)">
      <rect x="0" y="0" width="56" height="28" rx="8" fill="#f59e0b" />
      <text x="28" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">AWS</text>
      <rect x="64" y="0" width="76" height="28" rx="8" fill="#facc15" />
      <text x="102" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Firebase</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "tech-row1.svg"), "w", encoding="utf-8") as f:
    f.write(tech_row1)

tech_row2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 160" width="100%" height="100%">
  <style>
    @media (prefers-color-scheme: light) {
      .text-secondary { fill: #475569 !important; }
      .stroke-secondary { stroke: #475569 !important; }
    }
  </style>
  <defs>
    <linearGradient id="card-bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#110d1e" />
      <stop offset="100%" stop-color="#16112a" />
    </linearGradient>
  </defs>

  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="316" height="154" rx="16" fill="url(#card-bg2)" stroke="#3d2e70" stroke-width="1.5" />
    <text x="18" y="32" font-size="16">♾️</text>
    <text x="44" y="32" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">DevOps &amp; Deployment</text>
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="70" height="28" rx="8" fill="#0284c7" />
      <text x="35" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Docker</text>
      <rect x="78" y="0" width="90" height="28" rx="8" fill="#2563eb" />
      <text x="123" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Kubernetes</text>
      <rect x="176" y="0" width="106" height="28" rx="8" fill="#0ea5e9" />
      <text x="229" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">GitHub Actions</text>
    </g>
    <g transform="translate(16, 92)">
      <rect x="0" y="0" width="86" height="28" rx="8" fill="#9333ea" />
      <text x="43" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Terraform</text>
      <rect x="94" y="0" width="60" height="28" rx="8" fill="#16a34a" />
      <text x="124" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Nginx</text>
      <rect x="162" y="0" width="60" height="28" rx="8" fill="#4c3a8c" />
      <text x="192" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">CI/CD</text>
    </g>
  </g>

  <g transform="translate(334, 0)">
    <rect x="2" y="2" width="376" height="154" rx="16" fill="url(#card-bg2)" stroke="#3d2e70" stroke-width="1.5" />
    <text x="18" y="32" font-size="16">🔧</text>
    <text x="44" y="32" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="700" fill="#f8fafc">Languages &amp; Tools</text>
    <g transform="translate(16, 52)">
      <rect x="0" y="0" width="56" height="28" rx="8" fill="#f97316" />
      <text x="28" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">Java</text>
      <rect x="64" y="0" width="68" height="28" rx="8" fill="#0ea5e9" />
      <text x="98" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">Python</text>
      <rect x="140" y="0" width="38" height="28" rx="8" fill="#0284c7" />
      <text x="159" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">C</text>
      <rect x="186" y="0" width="46" height="28" rx="8" fill="#2563eb" />
      <text x="209" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">C++</text>
    </g>
    <g transform="translate(16, 92)">
      <rect x="0" y="0" width="44" height="28" rx="8" fill="#ef4444" />
      <text x="22" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">Git</text>
      <rect x="52" y="0" width="70" height="28" rx="8" fill="#1c1535" stroke="#3d2e70" stroke-width="1" />
      <text x="87" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#f8fafc" text-anchor="middle">GitHub</text>
      <rect x="130" y="0" width="76" height="28" rx="8" fill="#0ea5e9" />
      <text x="168" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="600" fill="#ffffff" text-anchor="middle">VS Code</text>
      <rect x="214" y="0" width="74" height="28" rx="8" fill="#ea580c" />
      <text x="251" y="18" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">Postman</text>
    </g>
  </g>

  <!-- Doodle -->
  <g transform="translate(735, 12)">
    <g font-family="'Segoe Print', 'Caveat', 'Comic Sans MS', cursive, sans-serif" font-size="16" font-weight="bold" class="text-secondary" fill="#c4b5fd" opacity="0.9">
      <text x="35" y="24" transform="rotate(-12 35 24)">Code</text>
      <text x="48" y="46" transform="rotate(-10 48 46)">Deploy</text>
      <text x="62" y="68" transform="rotate(-9 62 68)">Improve</text>
      <text x="75" y="90" transform="rotate(-8 75 90)">Repeat ♡</text>
    </g>
    <path d="M78 98 Q125 106 142 92" fill="none" class="stroke-secondary" stroke="#d946ef" stroke-width="2" opacity="0.8" />
    <polygon points="144,88 143,96 138,92" class="text-secondary" fill="#d946ef" opacity="0.8" />
    <g transform="translate(142, 70)" class="stroke-secondary" stroke="#c4b5fd" stroke-width="1.8" fill="none" opacity="0.9">
      <path d="M6 32 C3 20 5 12 12 12 L17 4 L26 12 C30 12 34 12 38 12 L47 4 L52 12 C59 12 61 20 58 32 C55 42 45 44 32 44 C19 44 9 42 6 32 Z" />
      <path d="M18 24 Q23 20 28 24" />
      <path d="M36 24 Q41 20 46 24" />
      <path d="M32 28 L30 32 L34 32 Z" class="text-secondary" fill="#c4b5fd" />
      <path d="M32 32 Q29 36 26 34" />
      <path d="M32 32 Q35 36 38 34" />
      <line x1="8" y1="26" x2="2" y2="24" />
      <line x1="8" y1="30" x2="1" y2="31" />
      <line x1="56" y1="26" x2="62" y2="24" />
      <line x1="56" y1="30" x2="63" y2="31" />
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "tech-row2.svg"), "w", encoding="utf-8") as f:
    f.write(tech_row2)

print("Generated new SVGs with Cute Soft Midnight theme!")
