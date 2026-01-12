extends CharacterBody2D


const SPEED = 400.0
const JUMP_VELOCITY = -400.0

func _physics_process(delta: float) -> void:
	# Adds gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta
	
	# Get the input direction and handle the movement/deceleration.
	var direction := Input.get_axis("left", "right")
	if direction:
		velocity.x = direction * SPEED
		# Plays animations depending on what direction the player is moving
		$AnimatedSprite2D.play("turning")
		$AnimatedSprite2D.flip_h = direction < 0
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		$AnimatedSprite2D.play("default")
		
	move_and_slide()
