import os
import shutil
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).parent.parent
HOME = Path.home()

# Distribution Targets
TARGETS = {
    "cline": HOME / ".cline" / "skills",
    "kilo": HOME / ".kilo" / "skills",
    "amp": HOME / ".amp" / "skills",
    "opencode": HOME / ".opencode" / "skills",
    "claude": HOME / ".claude" / "skills",
    "antigravity": HOME / ".gemini" / "antigravity" / "skills",
}

def sync_plugins():
    print(f"Syncing knowledge-work-plugins from {REPO_ROOT}...")
    
    # Categories are directories in REPO_ROOT that contain a 'skills' subdirectory
    categories = [d for d in REPO_ROOT.iterdir() if d.is_dir() and (d / "skills").exists()]
    
    for target_name, target_base_path in TARGETS.items():
        print(f"  Syncing to {target_name} ({target_base_path})...")
        
        for category_dir in categories:
            category_name = category_dir.name
            skills_dir = category_dir / "skills"
            
            for skill_dir in skills_dir.iterdir():
                if not skill_dir.is_dir():
                    continue
                    
                skill_name = skill_dir.name
                qualified_skill_name = f"{category_name}-{skill_name}"
                
                target_skill_dir = target_base_path / qualified_skill_name
                target_skill_dir.mkdir(parents=True, exist_ok=True)
                
                # Source SKILL.md
                source_skill_md = skill_dir / "SKILL.md"
                if not source_skill_md.exists():
                    continue
                    
                # Target SKILL.md
                target_skill_md = target_skill_dir / "SKILL.md"
                
                # Read content and inject metadata
                content = source_skill_md.read_text(encoding="utf-8")
                
                # Basic metadata injection
                today = "2026-02-14"
                metadata_lines = [
                    "adapter_metadata:",
                    f"  skill_name: {qualified_skill_name}",
                    "  skill_version: 1.0.0",
                    f"  last_synced: {today}",
                    f"  source_path: {category_name}/skills/{skill_name}/SKILL.md",
                    f"  adapter_id: {target_name}",
                    f"  adapter_format: {target_name.capitalize()} skill"
                ]
                metadata = "\n".join(metadata_lines)

                # Handle YAML frontmatter
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        new_content = f"---{parts[1]}{metadata}\n---{parts[2]}"
                    else:
                        new_content = f"---\n{metadata}\n---" + content
                else:
                    new_content = f"---\n{metadata}\n---\n\n" + content
                    
                target_skill_md.write_text(new_content, encoding="utf-8")
                
    print("\nSync Complete.")

if __name__ == "__main__":
    sync_plugins()
